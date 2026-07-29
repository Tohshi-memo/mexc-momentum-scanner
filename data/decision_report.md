# Decision Report

- generated_at: 2026-07-29T18:41:38.528931+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9821**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9821, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.18% | **-0.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.13% | **+0.68%** |
| LIMIT_4PCT | 12/20 | 60.0% | +1.00% | **+0.60%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.49% | **+0.44%** |
| LIMIT_BB3S | 3/19 | 15.8% | +2.50% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.32% | **+1.25%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.35% | **+1.02%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.30% | **+0.78%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.99% | **+0.50%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.78% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$119.27** / 初期 $100.00 (+19.27%)
- 確定トレード: 162件 (TP 63 / SL 94 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $119.27
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2863件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$138.74** / 初期 $100.00 (+38.74%)
- 確定: 1236件 (Win 343 / Loss 278 / Flat 615) / skip 1996件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0087 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SNXX/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $138.74

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.01** / 初期 $100.00 (+9.01%)
- 確定: 766件 (Win 246 / Loss 297 / Flat 223) / pending 0件 / skip 528件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $109.01

## 6. Latest Market Context

- 更新: 2026-07-29T18:41:24.298186+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64208.1
- Funnel: target 911 → liquid 170 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DIA/USDT:USDT | +16.75% | $1,766,327.25 |
| KORU/USDT:USDT | +14.23% | $69,790,857.75 |
| RE/USDT:USDT | +12.11% | $3,267,633.85 |
| SNXX/USDT:USDT | +11.41% | $8,465,482.77 |
| LAB/USDT:USDT | +8.60% | $1,992,544.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +3.91% | +3.97% |
| RAVE/USDT:USDT | below_1h_threshold | +3.76% | +3.82% |
| BESTOCK/USDT:USDT | below_1h_threshold | +3.48% | +3.54% |
| AEON1/USDT:USDT | below_1h_threshold | +3.02% | +3.08% |
| SOXL/USDT:USDT | below_1h_threshold | +2.90% | +2.96% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
