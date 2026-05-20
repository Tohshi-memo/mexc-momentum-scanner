# Decision Report

- generated_at: 2026-05-20T09:48:49.653580+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4537**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4537, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.82% | **-0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 13/20 | 65.0% | +0.73% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.14% | **-0.11%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |
| LIMIT_7PCT | 3/20 | 15.0% | -1.73% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| ASK_LONG | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.59%** |
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +0.44% | **+0.29%** |
| LIMIT_7PCT_LONG | 5/20 | 25.0% | +0.38% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$126.27** / 初期 $100.00 (+26.27%)
- 確定: 499件 (Win 131 / Loss 170 / Flat 198) / skip 599件
- 成長率目線: 平均log +0.000467 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $126.27

## 4. Latest Market Context

- 更新: 2026-05-20T09:48:44.596667+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=77465.8
- Funnel: target 762 → liquid 133 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.1 >= 65=1, 4h RSI 68.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +111.32% | $1,535,260.57 |
| PROMPT/USDT:USDT | +35.34% | $12,525,642.94 |
| FIDA/USDT:USDT | +31.05% | $2,778,699.17 |
| EDEN/USDT:USDT | +27.74% | $21,990,940.85 |
| LIT/USDT:USDT | +23.46% | $8,767,803.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EDEN/USDT:USDT | below_1h_threshold | +3.56% | +3.52% |
| DASH/USDT:USDT | below_1h_threshold | +2.91% | +2.87% |
| BSB/USDT:USDT | below_1h_threshold | +2.45% | +2.40% |
| VVV/USDT:USDT | below_1h_threshold | +1.45% | +1.40% |
| ZEC/USDT:USDT | below_1h_threshold | +1.39% | +1.35% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
