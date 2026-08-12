# Decision Report

- generated_at: 2026-08-12T22:06:18.578567+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11401**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=11401, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 2/15 | 13.3% | +8.00% | **+1.07%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.63% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.38% | **+1.31%** |
| LIMIT_BB3S_LONG | 2/4 | 50.0% | +2.38% | **+1.19%** |
| MARKET_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$606.08** / 初期 $100.00 (+506.08%)
- 確定: 3949件 (Win 1232 / Loss 1291 / Flat 1426) / skip 4013件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $606.08

## 4. Robust Adaptive DryRun ($100)

- 残高: **$147.30** / 初期 $100.00 (+47.30%)
- 確定: 1596件 (Win 449 / Loss 374 / Flat 773) / skip 3216件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0130 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $147.30

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.00** / 初期 $100.00 (+15.00%)
- 確定: 1410件 (Win 416 / Loss 535 / Flat 459) / pending 3件 / skip 1459件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000146 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_10PCT_LONG` EXPIRED account +0.00% 残高後 $115.00

## 6. Latest Market Context

- 更新: 2026-08-12T22:06:09.027874+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=63452.6
- Funnel: target 972 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +32.06% | $6,845,146.78 |
| BTW/USDT:USDT | +19.90% | $20,592,314.12 |
| BEAT/USDT:USDT | +15.96% | $64,729,836.09 |
| APR/USDT:USDT | +10.90% | $10,012,906.26 |
| VELVET/USDT:USDT | +10.64% | $19,668,863.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +2.49% | +2.47% |
| BEAT/USDT:USDT | below_1h_threshold | +2.37% | +2.35% |
| ONE/USDT:USDT | below_1h_threshold | +1.80% | +1.78% |
| BMT/USDT:USDT | below_1h_threshold | +1.14% | +1.12% |
| CYS/USDT:USDT | below_1h_threshold | +1.09% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
