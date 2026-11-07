# Decision Report

- generated_at: 2026-11-07T01:06:20.444391+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18341**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18341, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +0.65% | **+0.45%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.08% | **+0.38%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.35% | **+0.34%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.10% | **+0.88%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,478.52** / 初期 $100.00 (+1378.52%)
- 確定: 7040件 (Win 2025 / Loss 2248 / Flat 2767) / skip 7862件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.50% 残高後 $1,478.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$390.18** / 初期 $100.00 (+290.18%)
- 確定: 4711件 (Win 1269 / Loss 1039 / Flat 2403) / skip 7041件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0426 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $390.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6504件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000202 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T01:06:09.942082+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=75907.1
- Funnel: target 1089 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +41.48% | $54,828,584.02 |
| AIN/USDT:USDT | +23.00% | $4,473,758.98 |
| ONE/USDT:USDT | +17.87% | $12,620,604.86 |
| LYN/USDT:USDT | +11.34% | $1,567,483.20 |
| BTW/USDT:USDT | +8.93% | $7,128,887.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LYN/USDT:USDT | below_1h_threshold | +2.38% | +2.33% |
| ARIA/USDT:USDT | below_1h_threshold | +1.11% | +1.06% |
| SPX/USDT:USDT | below_1h_threshold | +1.03% | +0.98% |
| MUU/USDT:USDT | below_1h_threshold | +0.94% | +0.89% |
| MVLL/USDT:USDT | below_1h_threshold | +0.92% | +0.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
