# Decision Report

- generated_at: 2026-08-23T21:11:33.381835+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12470**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12470, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.92% | **-1.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_BB3S | 8/13 | 61.5% | +0.60% | **+0.37%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +0.51% | **+0.30%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.31% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/6 | 83.3% | +5.34% | **+4.45%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +4.30% | **+2.37%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +3.58% | **+2.15%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +4.67% | **+1.87%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.09% | **+1.85%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$721.85** / 初期 $100.00 (+621.85%)
- 確定: 4497件 (Win 1373 / Loss 1470 / Flat 1654) / skip 4534件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_4PCT_LONG` TP_HIT account +1.00% 残高後 $721.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.81** / 初期 $100.00 (+57.81%)
- 確定: 1946件 (Win 536 / Loss 468 / Flat 942) / skip 3935件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0098 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TUT/USDT:USDT `LIMIT_FIB1272` TP_HIT account +0.69% 残高後 $157.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.95** / 初期 $100.00 (+16.95%)
- 確定: 1866件 (Win 551 / Loss 707 / Flat 608) / pending 2件 / skip 2081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000133 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TAC/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.04% 残高後 $116.95

## 6. Latest Market Context

- 更新: 2026-08-23T21:11:22.473266+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=77620.0
- Funnel: target 1018 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +14.51% | $2,786,559.02 |
| PENGU/USDT:USDT | +14.05% | $19,121,663.30 |
| TUT/USDT:USDT | +12.21% | $60,623,270.96 |
| 1000RATS/USDT:USDT | +11.83% | $2,130,311.78 |
| BRETT/USDT:USDT | +11.20% | $1,314,611.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +3.84% | +3.53% |
| AAVE/USDT:USDT | below_1h_threshold | +2.38% | +2.06% |
| DASH/USDT:USDT | below_1h_threshold | +1.80% | +1.49% |
| STX/USDT:USDT | below_1h_threshold | +1.73% | +1.42% |
| WIF/USDT:USDT | below_1h_threshold | +1.70% | +1.38% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
