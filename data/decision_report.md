# Decision Report

- generated_at: 2026-08-12T03:06:22.431345+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11326**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11326, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.06% | **-1.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 19/20 | 95.0% | -0.10% | **-0.10%** |
| LIMIT_6PCT | 5/20 | 25.0% | -0.47% | **-0.12%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.85% | **-0.13%** |
| LIMIT_9PCT | 3/20 | 15.0% | -1.14% | **-0.17%** |
| LIMIT_8PCT | 3/20 | 15.0% | -1.43% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/5 | 40.0% | +8.00% | **+3.20%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.76% | **+1.40%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.88% | **+1.31%** |
| MARKET_LONG | 20/20 | 100.0% | +0.91% | **+0.91%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.47% | **+0.81%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 180件 (TP 69 / SL 106 / EXP 5)
- 最新: JIMOTHY/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$616.77** / 初期 $100.00 (+516.77%)
- 確定: 3940件 (Win 1230 / Loss 1285 / Flat 1425) / skip 3947件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $616.77

## 4. Robust Adaptive DryRun ($100)

- 残高: **$143.44** / 初期 $100.00 (+43.44%)
- 確定: 1569件 (Win 437 / Loss 364 / Flat 768) / skip 3168件
- 成長率目線: 平均log +0.000230 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DODO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $143.44

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.43** / 初期 $100.00 (+14.43%)
- 確定: 1344件 (Win 408 / Loss 528 / Flat 408) / pending 3件 / skip 1452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000111 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $114.43

## 6. Latest Market Context

- 更新: 2026-08-12T03:06:13.335030+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=63759.5
- Funnel: target 967 → liquid 189 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PROM/USDT:USDT | +58.46% | $6,399,748.82 |
| HOLO/USDT:USDT | +33.78% | $5,924,322.76 |
| JIMOTHY/USDT:USDT | +30.69% | $1,870,848.72 |
| LSK/USDT:USDT | +17.23% | $3,444,065.82 |
| CRWVSTOCK/USDT:USDT | +16.97% | $3,887,529.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JIMOTHY/USDT:USDT | below_1h_threshold | +3.87% | +3.81% |
| SNXX/USDT:USDT | below_1h_threshold | +2.53% | +2.47% |
| MUU/USDT:USDT | below_1h_threshold | +2.29% | +2.23% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +2.08% | +2.02% |
| BEAT/USDT:USDT | below_1h_threshold | +1.94% | +1.88% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
