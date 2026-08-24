# Decision Report

- generated_at: 2026-08-24T08:31:25.415444+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12501**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12501, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/18 | 44.4% | +0.73% | **+0.33%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.34% | **+0.27%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.20% | **+0.18%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.45% | **+0.45%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.31% | **+0.23%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.24% | **+0.18%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.18% | **+0.09%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.09% | **+0.04%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4509件 (Win 1375 / Loss 1477 / Flat 1657) / skip 4553件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1965件 (Win 536 / Loss 470 / Flat 959) / skip 3947件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: GPS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.65** / 初期 $100.00 (+16.65%)
- 確定: 1885件 (Win 556 / Loss 713 / Flat 616) / pending 5件 / skip 2084件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000043 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.65

## 6. Latest Market Context

- 更新: 2026-08-24T08:31:16.312962+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.49% price=76920.0
- Funnel: target 1019 → liquid 180 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PONS/USDT:USDT | +66.72% | $1,265,140.78 |
| TUT/USDT:USDT | +35.71% | $51,943,194.10 |
| PROM/USDT:USDT | +33.69% | $10,658,758.80 |
| PORTAL/USDT:USDT | +18.34% | $2,803,140.50 |
| UAI/USDT:USDT | +17.96% | $11,353,387.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CYS/USDT:USDT | below_1h_threshold | +4.00% | +4.49% |
| BLESS/USDT:USDT | below_1h_threshold | +3.55% | +4.05% |
| EUL/USDT:USDT | below_1h_threshold | +3.18% | +3.67% |
| PORTAL/USDT:USDT | below_1h_threshold | +1.70% | +2.19% |
| ON/USDT:USDT | below_1h_threshold | +1.58% | +2.07% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
