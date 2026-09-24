# Decision Report

- generated_at: 2026-09-24T14:56:32.543441+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15481**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15481, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.97% | **+0.44%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.98% | **+0.20%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.06% | **+0.03%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.19% | **-0.14%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.49% | **-0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +1.13% | **+0.80%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +1.03% | **+0.31%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +0.54% | **+0.30%** |

## 2. $100 Live Portfolio

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定トレード: 218件 (TP 79 / SL 134 / EXP 5)
- 最新: LSK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.20
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5899件 (Win 1739 / Loss 1890 / Flat 2270) / skip 6143件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONDO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$254.04** / 初期 $100.00 (+154.04%)
- 確定: 3428件 (Win 947 / Loss 791 / Flat 1690) / skip 5464件
- 成長率目線: 平均log +0.000272 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0389 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NOM/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $254.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.27** / 初期 $100.00 (+21.27%)
- 確定: 3159件 (Win 932 / Loss 1246 / Flat 981) / pending 0件 / skip 3796件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000158 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $121.27

## 6. Latest Market Context

- 更新: 2026-09-24T14:56:21.337670+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.60% price=83708.2
- Funnel: target 1069 → liquid 186 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NOM/USDT:USDT | +36.72% | $5,780,048.56 |
| LSK/USDT:USDT | +29.97% | $14,882,175.21 |
| LTC/USDT:USDT | +22.28% | $96,974,191.73 |
| ONDO/USDT:USDT | +19.63% | $69,229,666.20 |
| NIL/USDT:USDT | +18.00% | $26,283,847.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FET/USDT:USDT | below_1h_threshold | +4.71% | +5.32% |
| OP/USDT:USDT | below_1h_threshold | +3.89% | +4.49% |
| APT/USDT:USDT | below_1h_threshold | +3.06% | +3.67% |
| MYX/USDT:USDT | below_1h_threshold | +3.04% | +3.64% |
| XPL/USDT:USDT | below_1h_threshold | +2.47% | +3.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
