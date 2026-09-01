# Decision Report

- generated_at: 2026-09-01T18:21:20.887494+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13255**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13255, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.12% | **-0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.66% | **+0.59%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.97% | **+0.49%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.99% | **+0.45%** |
| LIMIT_6PCT | 4/20 | 20.0% | +2.03% | **+0.41%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.95% | **+0.95%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.96% | **+0.86%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.75% | **+0.56%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +0.47% | **+0.19%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +0.10% | **+0.03%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$787.97** / 初期 $100.00 (+687.97%)
- 確定: 4890件 (Win 1487 / Loss 1614 / Flat 1789) / skip 4926件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $787.97

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.47** / 初期 $100.00 (+73.47%)
- 確定: 2234件 (Win 622 / Loss 539 / Flat 1073) / skip 4432件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0271 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $173.47

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.08** / 初期 $100.00 (+15.08%)
- 確定: 2088件 (Win 610 / Loss 816 / Flat 662) / pending 1件 / skip 2638件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000148 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.08

## 6. Latest Market Context

- 更新: 2026-09-01T18:21:11.515889+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.25% price=77048.6
- Funnel: target 1036 → liquid 160 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FILECOIN/USDT:USDT | +8.82% | $7,565,670.22 |
| BTW/USDT:USDT | +5.33% | $3,109,339.87 |
| TUT/USDT:USDT | +5.14% | $4,030,361.02 |
| MAGMA/USDT:USDT | +4.60% | $1,760,760.47 |
| BEAT/USDT:USDT | +4.27% | $5,118,808.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +4.22% | +4.47% |
| UAI/USDT:USDT | below_1h_threshold | +2.81% | +3.06% |
| USELESS/USDT:USDT | below_1h_threshold | +2.58% | +2.83% |
| SOXS/USDT:USDT | below_1h_threshold | +1.48% | +1.73% |
| BTW/USDT:USDT | below_1h_threshold | +1.35% | +1.60% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
