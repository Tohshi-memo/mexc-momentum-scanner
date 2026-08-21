# Decision Report

- generated_at: 2026-08-21T18:11:30.175148+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12232**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12232, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.35% | **-1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_BB3S | 5/16 | 31.2% | -0.02% | **-0.01%** |
| LIMIT_8PCT | 5/20 | 25.0% | -0.06% | **-0.01%** |
| LIMIT_5PCT | 7/20 | 35.0% | -0.16% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.50% | **+3.50%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +3.44% | **+2.58%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.59% | **+2.15%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.29% | **+1.94%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.61% | **+1.70%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$640.35** / 初期 $100.00 (+540.35%)
- 確定: 4362件 (Win 1337 / Loss 1434 / Flat 1591) / skip 4431件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BB/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $640.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.04** / 初期 $100.00 (+56.04%)
- 確定: 1844件 (Win 511 / Loss 438 / Flat 895) / skip 3799件
- 成長率目線: 平均log +0.000241 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0766 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.04

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1888件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000305 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T18:11:19.382692+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=77311.2
- Funnel: target 1018 → liquid 212 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +38.16% | $10,836,236.20 |
| JIMOTHY/USDT:USDT | +18.11% | $1,022,658.21 |
| BLESS/USDT:USDT | +10.56% | $6,820,294.47 |
| BEAT/USDT:USDT | +9.16% | $54,291,367.25 |
| PEPE/USDT:USDT | +8.05% | $387,082,887.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NEIROCTO/USDT:USDT | below_1h_threshold | +2.14% | +2.23% |
| GPS/USDT:USDT | below_1h_threshold | +2.12% | +2.21% |
| RED/USDT:USDT | below_1h_threshold | +2.06% | +2.15% |
| FLOKI/USDT:USDT | below_1h_threshold | +1.95% | +2.04% |
| FARTCOIN/USDT:USDT | below_1h_threshold | +1.90% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
