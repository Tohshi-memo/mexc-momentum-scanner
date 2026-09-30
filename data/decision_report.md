# Decision Report

- generated_at: 2026-09-30T11:11:19.209278+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15832**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15832, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.05%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.05% | **-0.05%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.25% | **+0.24%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_BB3S | 9/17 | 52.9% | +0.35% | **+0.18%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.52% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +0.56% | **+0.36%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.96% | **+0.34%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.35% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,221.11** / 初期 $100.00 (+1121.11%)
- 確定: 5988件 (Win 1766 / Loss 1926 / Flat 2296) / skip 6405件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MOVR/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $1,221.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3536件 (Win 974 / Loss 812 / Flat 1750) / skip 5707件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0230 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 3992件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000233 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-09-30T11:11:08.365217+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.21% price=83698.4
- Funnel: target 1083 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +116.75% | $8,179,677.33 |
| MOVR/USDT:USDT | +65.87% | $2,729,087.54 |
| ARK/USDT:USDT | +48.78% | $1,779,409.63 |
| QNT/USDT:USDT | +20.15% | $338,871,330.93 |
| NIL/USDT:USDT | +16.67% | $2,385,794.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +2.08% | +2.29% |
| OKTASTOCK/USDT:USDT | below_1h_threshold | +1.05% | +1.26% |
| QNT/USDT:USDT | below_1h_threshold | +0.91% | +1.12% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.70% | +0.92% |
| SI/USDT:USDT | below_1h_threshold | +0.43% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
