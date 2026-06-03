# Decision Report

- generated_at: 2026-06-03T10:22:59.555620+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5539**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5539, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_ATR | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.62% | **+0.52%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.17% | **+0.41%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.57% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.92% | **+0.87%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.61% | **+0.80%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.96% | **+0.67%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.05% | **+0.63%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.02% | **+0.46%** |

## 2. $100 Live Portfolio

- 残高: **$96.61** / 初期 $100.00 (-3.39%)
- 確定トレード: 90件 (TP 26 / SL 61 / EXP 3)
- 最新: VVV/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.61
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.71** / 初期 $100.00 (+31.71%)
- 確定: 993件 (Win 236 / Loss 306 / Flat 451) / skip 1107件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $131.71

## 4. Latest Market Context

- 更新: 2026-06-03T10:22:57.034522+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=67191.1
- Funnel: target 771 → liquid 151 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLO/USDT:USDT | +37.58% | $4,245,655.60 |
| EPIC/USDT:USDT | +29.18% | $2,456,036.45 |
| PORTAL/USDT:USDT | +26.16% | $14,749,200.17 |
| APR/USDT:USDT | +24.98% | $1,420,423.20 |
| ENA/USDT:USDT | +24.43% | $54,996,112.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIA/USDT:USDT | below_1h_threshold | +2.18% | +1.95% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +2.02% | +1.80% |
| MYX/USDT:USDT | below_1h_threshold | +1.83% | +1.60% |
| OP/USDT:USDT | below_1h_threshold | +1.74% | +1.51% |
| ENA/USDT:USDT | below_1h_threshold | +1.67% | +1.45% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
