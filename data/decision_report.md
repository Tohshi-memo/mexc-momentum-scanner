# Decision Report

- generated_at: 2026-08-20T17:06:18.513896+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12061**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12061, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.93% | **-0.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | -1.09% | **-0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.73% | **+1.30%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.52% | **+0.91%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +0.77% | **+0.42%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +0.44% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 188件 (TP 72 / SL 111 / EXP 5)
- 最新: VELVET/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$600.96** / 初期 $100.00 (+500.96%)
- 確定: 4274件 (Win 1307 / Loss 1397 / Flat 1570) / skip 4348件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.20%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $600.96

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1822件 (Win 502 / Loss 429 / Flat 891) / skip 3650件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $154.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.48** / 初期 $100.00 (+16.48%)
- 確定: 1758件 (Win 521 / Loss 673 / Flat 564) / pending 1件 / skip 1777件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000051 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.48

## 6. Latest Market Context

- 更新: 2026-08-20T17:06:09.673914+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=72707.0
- Funnel: target 1011 → liquid 200 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PEOPLE/USDT:USDT | +8.35% | $1,436,917.44 |
| ONG/USDT:USDT | +6.69% | $4,389,017.74 |
| ALLO/USDT:USDT | +5.01% | $2,383,862.26 |
| XRP/USDT:USDT | +3.98% | $1,030,865,535.33 |
| PIPPIN/USDT:USDT | +3.78% | $1,992,799.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.13% | +2.26% |
| HUTSTOCK/USDT:USDT | below_1h_threshold | +1.67% | +1.79% |
| MVLL/USDT:USDT | below_1h_threshold | +1.55% | +1.68% |
| COINBASE/USDT:USDT | below_1h_threshold | +1.35% | +1.48% |
| LITESTOCK/USDT:USDT | below_1h_threshold | +1.10% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
