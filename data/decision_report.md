# Decision Report

- generated_at: 2026-06-01T10:20:47.495364+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5302**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5302, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +0.85% | **+0.72%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |
| ASK | 20/20 | 100.0% | +0.35% | **+0.35%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.34% | **+0.31%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.75% | **+0.79%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.10% | **+0.41%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.26% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 969件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T10:20:44.698557+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=72742.8
- Funnel: target 775 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PORTAL/USDT:USDT | +143.91% | $35,651,190.56 |
| H/USDT:USDT | +97.11% | $31,090,274.44 |
| SLX/USDT:USDT | +93.20% | $6,871,547.54 |
| LAB/USDT:USDT | +68.42% | $211,015,905.72 |
| WLD/USDT:USDT | +17.13% | $84,457,609.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PORTAL/USDT:USDT | below_1h_threshold | +4.30% | +4.45% |
| BILL/USDT:USDT | below_1h_threshold | +3.73% | +3.88% |
| BIANRENSHENG/USDT:USDT | below_1h_threshold | +2.51% | +2.66% |
| XLM/USDT:USDT | below_1h_threshold | +1.41% | +1.55% |
| TONCOIN/USDT:USDT | below_1h_threshold | +1.25% | +1.40% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
