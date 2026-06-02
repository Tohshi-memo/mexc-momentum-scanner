# Decision Report

- generated_at: 2026-06-02T16:05:13.948830+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5465**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5465, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.28% | **+0.26%** |
| ASK | 20/20 | 100.0% | +0.22% | **+0.22%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.31% | **+1.12%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.54% | **+1.00%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.85% | **+0.64%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +1.11% | **+0.61%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.52% | **+0.34%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 88件 (TP 26 / SL 59 / EXP 3)
- 最新: STG/USDT:USDT TP_HIT PnL +8.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.71** / 初期 $100.00 (+31.71%)
- 確定: 974件 (Win 229 / Loss 298 / Flat 447) / skip 1052件
- 成長率目線: 平均log +0.000283 / 幾何平均 +0.028% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $131.71

## 4. Latest Market Context

- 更新: 2026-06-02T16:05:11.118654+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.20% price=67411.4
- Funnel: target 773 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +2.11% | $4,628,244.83 |
| EDGE/USDT:USDT | +2.05% | $9,778,035.56 |
| BSB/USDT:USDT | +2.02% | $5,748,334.52 |
| APE/USDT:USDT | +1.79% | $3,421,701.80 |
| CHIP/USDT:USDT | +1.78% | $4,644,064.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +2.11% | +1.91% |
| BSB/USDT:USDT | below_1h_threshold | +2.03% | +1.83% |
| APE/USDT:USDT | below_1h_threshold | +1.79% | +1.59% |
| CHIP/USDT:USDT | below_1h_threshold | +1.79% | +1.58% |
| EDGE/USDT:USDT | below_1h_threshold | +1.64% | +1.43% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
