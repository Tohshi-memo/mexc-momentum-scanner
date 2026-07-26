# Decision Report

- generated_at: 2026-07-26T10:31:16.143501+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9569**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9569, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +0.70% | **+0.67%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.33% | **+0.67%** |
| LIMIT_BB3S | 3/18 | 16.7% | +2.88% | **+0.48%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.26% | **+0.44%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.08% | **+0.31%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.94% | **+5.94%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.30% | **+0.71%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.57% | **+0.64%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.11% | **+0.42%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.14% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$457.12** / 初期 $100.00 (+357.12%)
- 確定: 3397件 (Win 1078 / Loss 1104 / Flat 1215) / skip 2733件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $457.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.72** / 初期 $100.00 (+37.72%)
- 確定: 1222件 (Win 338 / Loss 274 / Flat 610) / skip 1758件
- 成長率目線: 平均log +0.000262 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0693 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $137.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.66** / 初期 $100.00 (+8.66%)
- 確定: 612件 (Win 206 / Loss 235 / Flat 171) / pending 4件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $108.66

## 6. Latest Market Context

- 更新: 2026-07-26T10:31:10.846405+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=64496.5
- Funnel: target 898 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +63.56% | $38,679,648.08 |
| DIA/USDT:USDT | +47.33% | $3,195,790.06 |
| PIEVERSE/USDT:USDT | +42.31% | $4,803,682.60 |
| BANK/USDT:USDT | +27.20% | $93,477,393.63 |
| KAITO/USDT:USDT | +16.40% | $3,706,456.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KAITO/USDT:USDT | below_1h_threshold | +3.67% | +3.69% |
| RIF/USDT:USDT | below_1h_threshold | +2.32% | +2.34% |
| ZAMA/USDT:USDT | below_1h_threshold | +2.12% | +2.14% |
| AAVE/USDT:USDT | below_1h_threshold | +1.85% | +1.87% |
| VELVET/USDT:USDT | below_1h_threshold | +1.38% | +1.40% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
