# Decision Report

- generated_at: 2026-08-21T20:41:35.753431+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12253**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12253, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.07% | **-0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/17 | 58.8% | +3.65% | **+2.15%** |
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

- 残高: **$656.45** / 初期 $100.00 (+556.45%)
- 確定: 4376件 (Win 1340 / Loss 1435 / Flat 1601) / skip 4438件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $656.45

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.96** / 初期 $100.00 (+55.96%)
- 確定: 1861件 (Win 514 / Loss 444 / Flat 903) / skip 3803件
- 成長率目線: 平均log +0.000239 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0633 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $155.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1907件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000205 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T20:41:24.143785+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.54% price=77411.4
- Funnel: target 1018 → liquid 218 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.4 >= 65=1, 4h RSI 89.6 >= 65=1, 4h RSI 69.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +227.83% | $2,063,186.37 |
| CATE/USDT:USDT | +31.01% | $11,156,727.83 |
| JIMOTHY/USDT:USDT | +30.58% | $1,467,624.96 |
| COTI/USDT:USDT | +14.52% | $3,129,964.38 |
| MAGMA/USDT:USDT | +13.14% | $1,861,443.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_relative_strength | +5.17% | +4.63% |
| TRB/USDT:USDT | below_1h_threshold | +4.35% | +3.81% |
| ONT/USDT:USDT | below_1h_threshold | +3.83% | +3.28% |
| ZEC/USDT:USDT | below_1h_threshold | +3.81% | +3.27% |
| STX/USDT:USDT | below_1h_threshold | +3.72% | +3.18% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
