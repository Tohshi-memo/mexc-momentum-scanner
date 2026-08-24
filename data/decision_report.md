# Decision Report

- generated_at: 2026-08-24T15:11:25.123245+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12519**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.21% / filled 20/20。**
- 全期間 MARKET基準: n=12519, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.81% | **+0.72%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 2/20 | 10.0% | +4.94% | **+0.49%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.66% | **+0.43%** |
| MARKET | 20/20 | 100.0% | +0.21% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.98% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.58% | **+0.58%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +1.38% | **+0.21%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.31% | **+0.17%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4510件 (Win 1375 / Loss 1477 / Flat 1658) / skip 4570件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1972件 (Win 536 / Loss 470 / Flat 966) / skip 3958件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0067 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.26** / 初期 $100.00 (+16.26%)
- 確定: 1902件 (Win 559 / Loss 719 / Flat 624) / pending 5件 / skip 2084件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000289 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: STORJ/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.26

## 6. Latest Market Context

- 更新: 2026-08-24T15:11:16.109384+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=79553.9
- Funnel: target 1022 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +72.89% | $1,560,280.61 |
| CASHCAT/USDT:USDT | +46.59% | $1,457,890.17 |
| PROM/USDT:USDT | +29.00% | $13,158,017.96 |
| SUPER/USDT:USDT | +25.58% | $3,726,891.43 |
| UAI/USDT:USDT | +24.24% | $14,351,078.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRCLSTOCK/USDT:USDT | below_1h_threshold | +4.17% | +4.08% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +3.10% | +3.00% |
| MONAD/USDT:USDT | below_1h_threshold | +2.95% | +2.86% |
| PORTAL/USDT:USDT | below_1h_threshold | +2.69% | +2.60% |
| BASECAT/USDT:USDT | below_1h_threshold | +2.24% | +2.15% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
