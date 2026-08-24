# Decision Report

- generated_at: 2026-08-24T18:51:50.419659+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12538**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12538, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.35% | **+0.31%** |
| LIMIT_8PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_9PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_7PCT | 5/20 | 25.0% | -0.24% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +5.33% | **+2.40%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +5.21% | **+2.08%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +6.31% | **+1.89%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.83% | **+1.72%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +7.67% | **+1.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$692.27** / 初期 $100.00 (+592.27%)
- 確定: 4523件 (Win 1379 / Loss 1483 / Flat 1661) / skip 4576件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CATE/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $692.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.16** / 初期 $100.00 (+56.16%)
- 確定: 1973件 (Win 536 / Loss 471 / Flat 966) / skip 3976件
- 成長率目線: 平均log +0.000226 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.16

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.44** / 初期 $100.00 (+15.44%)
- 確定: 1909件 (Win 560 / Loss 725 / Flat 624) / pending 4件 / skip 2105件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000066 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `MARKET` TP_HIT account +0.34% 残高後 $115.44

## 6. Latest Market Context

- 更新: 2026-08-24T18:51:38.782329+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=78991.0
- Funnel: target 1022 → liquid 184 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.9 >= 65=1, 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +72.98% | $1,978,387.53 |
| STORJ/USDT:USDT | +8.46% | $3,915,778.42 |
| MONAD/USDT:USDT | +8.15% | $2,895,723.92 |
| TUT/USDT:USDT | +6.22% | $62,864,981.34 |
| XMR/USDT:USDT | +6.20% | $5,163,882.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 1000RATS/USDT:USDT | below_1h_threshold | +3.83% | +3.49% |
| XMR/USDT:USDT | below_1h_threshold | +3.10% | +2.76% |
| ONG/USDT:USDT | below_1h_threshold | +3.03% | +2.69% |
| BEAT/USDT:USDT | below_1h_threshold | +2.37% | +2.04% |
| ONDO/USDT:USDT | below_1h_threshold | +2.20% | +1.87% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
