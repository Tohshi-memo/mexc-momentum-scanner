# Decision Report

- generated_at: 2026-09-02T01:06:29.709712+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13283**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13283, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.82% | **+0.82%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.02% | **+0.76%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +3.64% | **+2.36%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +3.17% | **+1.74%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +3.47% | **+1.21%** |
| LIMIT_2PCT_LONG | 19/20 | 95.0% | +1.26% | **+1.19%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.59% | **+1.04%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$823.83** / 初期 $100.00 (+723.83%)
- 確定: 4918件 (Win 1498 / Loss 1619 / Flat 1801) / skip 4926件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $823.83

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.69** / 初期 $100.00 (+74.69%)
- 確定: 2262件 (Win 632 / Loss 544 / Flat 1086) / skip 4432件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0955 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: FONE/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $174.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2665件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000315 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-02T01:06:19.746160+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77154.9
- Funnel: target 1036 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +25.84% | $16,957,993.16 |
| MAGMA/USDT:USDT | +22.74% | $4,499,196.39 |
| FONE/USDT:USDT | +22.22% | $1,343,915.25 |
| ACE/USDT:USDT | +15.47% | $10,336,357.94 |
| USELESS/USDT:USDT | +9.43% | $33,939,925.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UKOIL/USDT:USDT | below_1h_threshold | +1.60% | +1.63% |
| USOIL/USDT:USDT | below_1h_threshold | +1.43% | +1.47% |
| AKE/USDT:USDT | below_1h_threshold | +0.75% | +0.78% |
| NICKEL/USDT:USDT | below_1h_threshold | +0.71% | +0.74% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.69% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
