# Decision Report

- generated_at: 2026-09-01T21:01:23.437339+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13270**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13270, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.13% | **-1.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 5/20 | 25.0% | +6.28% | **+1.57%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +3.15% | **+1.42%** |
| LIMIT_7PCT | 5/20 | 25.0% | +4.88% | **+1.22%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.46% | **+0.80%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.88% | **+0.71%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.44% | **+0.65%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.29% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$814.67** / 初期 $100.00 (+714.67%)
- 確定: 4905件 (Win 1494 / Loss 1615 / Flat 1796) / skip 4926件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` SL_HIT account +0.17% 残高後 $814.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.80** / 初期 $100.00 (+74.80%)
- 確定: 2249件 (Win 629 / Loss 541 / Flat 1079) / skip 4432件
- 成長率目線: 平均log +0.000248 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0948 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $174.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2652件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000201 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-01T21:01:12.259617+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=77435.1
- Funnel: target 1036 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +46.37% | $1,653,873.03 |
| UAI/USDT:USDT | +27.23% | $8,112,403.29 |
| MAGMA/USDT:USDT | +16.25% | $2,645,584.86 |
| ACE/USDT:USDT | +9.56% | $7,218,899.68 |
| FILECOIN/USDT:USDT | +9.26% | $18,580,733.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +2.98% | +2.96% |
| BONER/USDT:USDT | below_1h_threshold | +2.14% | +2.12% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.37% | +1.34% |
| DESTOCK/USDT:USDT | below_1h_threshold | +0.58% | +0.56% |
| ONG/USDT:USDT | below_1h_threshold | +0.49% | +0.47% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
