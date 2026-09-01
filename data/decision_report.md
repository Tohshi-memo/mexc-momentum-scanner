# Decision Report

- generated_at: 2026-09-01T22:16:25.336264+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13272**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13272, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.70% | **-1.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 6/20 | 30.0% | +5.85% | **+1.76%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +3.10% | **+1.55%** |
| LIMIT_7PCT | 6/20 | 30.0% | +4.54% | **+1.36%** |
| LIMIT_6PCT | 7/20 | 35.0% | +3.63% | **+1.27%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.93% | **+1.93%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.44% | **+1.38%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.62% | **+1.29%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.91% | **+1.05%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.98% | **+0.99%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$817.41** / 初期 $100.00 (+717.41%)
- 確定: 4907件 (Win 1495 / Loss 1615 / Flat 1797) / skip 4926件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $817.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$175.07** / 初期 $100.00 (+75.07%)
- 確定: 2251件 (Win 630 / Loss 541 / Flat 1080) / skip 4432件
- 成長率目線: 平均log +0.000249 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0993 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $175.07

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.88** / 初期 $100.00 (+14.88%)
- 確定: 2089件 (Win 610 / Loss 817 / Flat 662) / pending 0件 / skip 2655件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000220 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: FILECOIN/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.88

## 6. Latest Market Context

- 更新: 2026-09-01T22:16:13.722554+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=77246.0
- Funnel: target 1036 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BONER/USDT:USDT | +46.41% | $1,932,685.49 |
| UAI/USDT:USDT | +22.81% | $13,008,502.93 |
| MAGMA/USDT:USDT | +17.66% | $2,918,397.69 |
| ACE/USDT:USDT | +10.33% | $8,098,849.47 |
| FILECOIN/USDT:USDT | +8.18% | $20,056,185.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.19% | +4.11% |
| CASHCAT/USDT:USDT | below_1h_threshold | +2.58% | +2.49% |
| UAI/USDT:USDT | below_1h_threshold | +2.30% | +2.22% |
| PYTH/USDT:USDT | below_1h_threshold | +0.91% | +0.83% |
| BICO/USDT:USDT | below_1h_threshold | +0.64% | +0.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
