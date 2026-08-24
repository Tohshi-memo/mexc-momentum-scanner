# Decision Report

- generated_at: 2026-08-24T12:16:25.910121+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12511**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12511, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.94% | **-0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 3/20 | 15.0% | +3.92% | **+0.59%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.62% | **+0.43%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.49% | **+0.20%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.36% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.73% | **+1.91%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.61% | **+1.70%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.00% | **+1.70%** |
| MARKET_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.76% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4510件 (Win 1375 / Loss 1477 / Flat 1658) / skip 4562件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1970件 (Win 536 / Loss 470 / Flat 964) / skip 3952件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0125 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.23** / 初期 $100.00 (+16.23%)
- 確定: 1894件 (Win 557 / Loss 717 / Flat 620) / pending 5件 / skip 2084件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000084 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $116.23

## 6. Latest Market Context

- 更新: 2026-08-24T12:16:17.070946+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=78184.3
- Funnel: target 1019 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +49.91% | $1,335,136.47 |
| PROM/USDT:USDT | +36.37% | $11,649,487.88 |
| PORTAL/USDT:USDT | +31.69% | $3,695,172.37 |
| CASHCAT/USDT:USDT | +29.24% | $1,144,204.03 |
| UAI/USDT:USDT | +23.62% | $12,923,497.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EGLD/USDT:USDT | below_1h_threshold | +1.18% | +1.49% |
| BASECAT/USDT:USDT | below_1h_threshold | +0.76% | +1.07% |
| SPK/USDT:USDT | below_1h_threshold | +0.62% | +0.93% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +0.51% | +0.82% |
| SUPER/USDT:USDT | below_1h_threshold | +0.37% | +0.68% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
