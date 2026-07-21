# Decision Report

- generated_at: 2026-07-21T02:16:26.158347+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9140**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.17% / filled 20/20。**
- 全期間 MARKET基準: n=9140, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 18/20 | 90.0% | +1.61% | **+1.45%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.74% | **+1.30%** |
| MARKET | 20/20 | 100.0% | +1.17% | **+1.17%** |
| LIMIT_7PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.97% | **+0.30%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.29% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$406.41** / 初期 $100.00 (+306.41%)
- 確定: 3202件 (Win 1002 / Loss 1019 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ERA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $406.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$128.15** / 初期 $100.00 (+28.15%)
- 確定: 1101件 (Win 288 / Loss 227 / Flat 586) / skip 1450件
- 成長率目線: 平均log +0.000225 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1203 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ERA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $128.15

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.27** / 初期 $100.00 (+1.27%)
- 確定: 335件 (Win 118 / Loss 148 / Flat 69) / pending 6件 / skip 273件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000260 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $101.27

## 6. Latest Market Context

- 更新: 2026-07-21T02:16:15.716685+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=65204.5
- Funnel: target 885 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ERA/USDT:USDT | +55.66% | $1,257,604.37 |
| JIMOTHY/USDT:USDT | +27.54% | $2,790,052.63 |
| BLESS/USDT:USDT | +15.16% | $1,702,956.01 |
| HEMI/USDT:USDT | +9.65% | $3,162,822.55 |
| LDO/USDT:USDT | +8.67% | $6,178,934.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.91% | +3.91% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +2.41% | +2.41% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.01% | +2.01% |
| EIGEN/USDT:USDT | below_1h_threshold | +1.10% | +1.10% |
| AXTISTOCK/USDT:USDT | below_1h_threshold | +1.07% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
