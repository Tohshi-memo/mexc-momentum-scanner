# Decision Report

- generated_at: 2026-07-21T07:46:30.062380+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9159**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9159, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.00% | **+0.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.97% | **+0.59%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.01% | **+0.40%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.11% | **+0.11%** |
| MARKET | 20/20 | 100.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/6 | 33.3% | +7.51% | **+2.50%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.18% | **+1.85%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.44% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.67% | **+0.67%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.97% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$421.46** / 初期 $100.00 (+321.46%)
- 確定: 3221件 (Win 1011 / Loss 1026 / Flat 1184) / skip 2499件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $421.46

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.31** / 初期 $100.00 (+31.31%)
- 確定: 1120件 (Win 297 / Loss 234 / Flat 589) / skip 1450件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0947 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $131.31

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 341件 (Win 120 / Loss 152 / Flat 69) / pending 0件 / skip 292件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000220 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T07:46:18.227849+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=66010.0
- Funnel: target 885 → liquid 175 → pre 50 → checked 50 → surge 5 → strict 2
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.3 >= 65=1, 4h RSI 77.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +123.35% | $3,962,089.18 |
| ERA/USDT:USDT | +47.75% | $5,951,901.54 |
| ZHIPUSTOCK/USDT:USDT | +33.56% | $2,902,220.45 |
| ON/USDT:USDT | +12.08% | $2,663,855.19 |
| BLESS/USDT:USDT | +10.80% | $2,437,356.59 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MVLL/USDT:USDT | below_1h_threshold | +3.46% | +3.28% |
| ONDO/USDT:USDT | below_1h_threshold | +2.56% | +2.38% |
| ALLO/USDT:USDT | below_1h_threshold | +1.95% | +1.77% |
| SOXL/USDT:USDT | below_1h_threshold | +1.83% | +1.66% |
| B/USDT:USDT | below_1h_threshold | +1.64% | +1.46% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
