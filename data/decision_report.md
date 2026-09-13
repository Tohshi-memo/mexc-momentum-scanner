# Decision Report

- generated_at: 2026-09-13T00:56:30.743987+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14335**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14335, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +4.80% | **+1.68%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.78% | **+0.98%** |
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.09% | **+0.27%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.30% | **+1.72%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +2.00% | **+1.40%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.65% | **+1.32%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.96% | **+1.28%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.74% | **+0.71%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5466件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$215.22** / 初期 $100.00 (+115.22%)
- 確定: 2853件 (Win 788 / Loss 663 / Flat 1402) / skip 4893件
- 成長率目線: 平均log +0.000269 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1314 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $215.22

## 5. Causal Adaptive DryRun ($100)

- 残高: **$124.91** / 初期 $100.00 (+24.91%)
- 確定: 2786件 (Win 826 / Loss 1071 / Flat 889) / pending 4件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000441 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $124.91

## 6. Latest Market Context

- 更新: 2026-09-13T00:56:18.267387+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=77237.6
- Funnel: target 1068 → liquid 123 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +50.11% | $59,029,107.60 |
| ZCAT/USDT:USDT | +26.99% | $1,051,767.75 |
| STORJ/USDT:USDT | +19.70% | $20,566,745.39 |
| REZ/USDT:USDT | +16.37% | $2,405,648.92 |
| ALCH/USDT:USDT | +14.32% | $2,474,123.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHZ/USDT:USDT | below_1h_threshold | +1.68% | +1.69% |
| NIULAI/USDT:USDT | below_1h_threshold | +1.55% | +1.55% |
| REZ/USDT:USDT | below_1h_threshold | +1.53% | +1.54% |
| INJ/USDT:USDT | below_1h_threshold | +1.15% | +1.16% |
| UAI/USDT:USDT | below_1h_threshold | +1.04% | +1.05% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
