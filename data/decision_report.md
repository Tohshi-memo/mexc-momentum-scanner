# Decision Report

- generated_at: 2026-05-20T03:53:54.796837+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4520**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4520, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.71% | **+1.09%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.52% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.50% | **+0.90%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +3.56% | **+0.71%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$125.04** / 初期 $100.00 (+25.04%)
- 確定: 482件 (Win 128 / Loss 166 / Flat 188) / skip 599件
- 成長率目線: 平均log +0.000464 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EDEN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $125.04

## 4. Latest Market Context

- 更新: 2026-05-20T03:53:47.325640+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=76703.1
- Funnel: target 764 → liquid 138 → pre 50 → checked 50 → surge 4 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1, 4h RSI 68.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +43.09% | $18,699,108.71 |
| PROMPT/USDT:USDT | +34.80% | $12,909,693.41 |
| LIT/USDT:USDT | +23.76% | $6,238,777.80 |
| FIDA/USDT:USDT | +15.05% | $1,355,922.73 |
| SPACE/USDT:USDT | +13.63% | $1,201,702.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +4.02% | +3.96% |
| VVV/USDT:USDT | below_1h_threshold | +3.02% | +2.96% |
| FIGHT/USDT:USDT | below_1h_threshold | +1.81% | +1.75% |
| RIVER/USDT:USDT | below_1h_threshold | +1.74% | +1.67% |
| HOME/USDT:USDT | below_1h_threshold | +1.70% | +1.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
