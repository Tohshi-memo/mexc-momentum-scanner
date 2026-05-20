# Decision Report

- generated_at: 2026-05-20T03:48:49.106888+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4519**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4519, expectancy=-0.09%
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
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_ATR | 10/20 | 50.0% | +1.08% | **+0.54%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.78% | **+0.53%** |

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
- 確定: 481件 (Win 128 / Loss 166 / Flat 187) / skip 599件
- 成長率目線: 平均log +0.000465 / 幾何平均 +0.046% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FIDA/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.90% 残高後 $125.04

## 4. Latest Market Context

- 更新: 2026-05-20T03:48:44.444264+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=76722.9
- Funnel: target 764 → liquid 138 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.8 >= 65=1, 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +36.04% | $18,314,432.36 |
| PROMPT/USDT:USDT | +34.99% | $12,905,124.37 |
| LIT/USDT:USDT | +24.22% | $6,207,535.44 |
| ZEST/USDT:USDT | +15.24% | $1,890,399.13 |
| FIDA/USDT:USDT | +14.30% | $1,351,474.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +4.29% | +4.20% |
| BLUAI/USDT:USDT | below_1h_threshold | +3.98% | +3.89% |
| VVV/USDT:USDT | below_1h_threshold | +2.97% | +2.88% |
| INJ/USDT:USDT | below_1h_threshold | +1.89% | +1.80% |
| HOME/USDT:USDT | below_1h_threshold | +1.85% | +1.76% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
