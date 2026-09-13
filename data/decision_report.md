# Decision Report

- generated_at: 2026-09-13T03:01:27.228096+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14357**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14357, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.11% | **-0.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 8/20 | 40.0% | +2.96% | **+1.19%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.64% | **+0.64%** |
| LIMIT_9PCT | 6/20 | 30.0% | +2.00% | **+0.60%** |
| LIMIT_7PCT | 8/20 | 40.0% | +0.70% | **+0.28%** |
| LIMIT_10PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/14 | 42.9% | +6.16% | **+2.64%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +4.99% | **+1.75%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +3.97% | **+1.59%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.78% | **+1.52%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.28% | **+1.21%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 211件 (TP 78 / SL 128 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,080.43** / 初期 $100.00 (+980.43%)
- 確定: 5430件 (Win 1635 / Loss 1760 / Flat 2035) / skip 5488件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,080.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$220.70** / 初期 $100.00 (+120.70%)
- 確定: 2875件 (Win 797 / Loss 671 / Flat 1407) / skip 4893件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0880 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $220.70

## 5. Causal Adaptive DryRun ($100)

- 残高: **$126.93** / 初期 $100.00 (+26.93%)
- 確定: 2808件 (Win 836 / Loss 1079 / Flat 893) / pending 3件 / skip 3016件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000493 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LSK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $126.93

## 6. Latest Market Context

- 更新: 2026-09-13T03:01:14.953586+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=77250.1
- Funnel: target 1068 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LSK/USDT:USDT | +184.66% | $69,002,232.00 |
| POWR/USDT:USDT | +44.62% | $1,441,201.71 |
| ZCAT/USDT:USDT | +30.42% | $1,137,196.41 |
| STORJ/USDT:USDT | +20.02% | $18,997,624.26 |
| ALCH/USDT:USDT | +16.41% | $2,714,319.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +2.41% | +2.43% |
| ILV/USDT:USDT | below_1h_threshold | +1.16% | +1.18% |
| UAI/USDT:USDT | below_1h_threshold | +0.64% | +0.66% |
| FLOCK/USDT:USDT | below_1h_threshold | +0.59% | +0.61% |
| ORCLSTOCK/USDT:USDT | below_1h_threshold | +0.41% | +0.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
