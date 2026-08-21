# Decision Report

- generated_at: 2026-08-21T20:46:31.367083+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12254**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12254, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.07% | **-0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 11/17 | 64.7% | +4.04% | **+2.62%** |
| LIMIT_6PCT | 7/20 | 35.0% | +4.54% | **+1.59%** |
| LIMIT_7PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.85% | **+1.66%** |
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +1.63% | **+1.63%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.40% | **+0.84%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +1.46% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$663.02** / 初期 $100.00 (+563.02%)
- 確定: 4377件 (Win 1341 / Loss 1435 / Flat 1601) / skip 4438件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $663.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.03** / 初期 $100.00 (+57.03%)
- 確定: 1862件 (Win 515 / Loss 444 / Flat 903) / skip 3803件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0801 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_6PCT` TP_HIT account +0.69% 残高後 $157.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1908件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T20:46:20.136214+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.51% price=77391.2
- Funnel: target 1018 → liquid 218 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.4 >= 65=1, 4h RSI 89.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +226.59% | $2,178,437.69 |
| CATE/USDT:USDT | +32.36% | $11,177,994.31 |
| JIMOTHY/USDT:USDT | +25.20% | $1,486,125.57 |
| MAGMA/USDT:USDT | +13.97% | $1,896,256.47 |
| COTI/USDT:USDT | +12.21% | $3,186,033.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +4.92% | +4.40% |
| TRB/USDT:USDT | below_1h_threshold | +4.02% | +3.50% |
| ROBO/USDT:USDT | below_1h_threshold | +3.78% | +3.27% |
| STX/USDT:USDT | below_1h_threshold | +3.61% | +3.09% |
| 1000BONK/USDT:USDT | below_1h_threshold | +3.48% | +2.97% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
