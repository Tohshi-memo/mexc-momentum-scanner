# Decision Report

- generated_at: 2026-08-21T21:31:27.319841+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12262**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12262, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.02% | **-0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 10/16 | 62.5% | +3.61% | **+2.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_6PCT | 5/20 | 25.0% | +5.55% | **+1.39%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.25% | **+1.19%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.88% | **+1.03%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.07% | **+0.93%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +0.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$653.12** / 初期 $100.00 (+553.12%)
- 確定: 4384件 (Win 1341 / Loss 1438 / Flat 1605) / skip 4439件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROBO/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $653.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.93** / 初期 $100.00 (+55.93%)
- 確定: 1869件 (Win 515 / Loss 446 / Flat 908) / skip 3804件
- 成長率目線: 平均log +0.000238 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0983 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ROBO/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $155.93

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1913件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000243 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T21:31:16.325924+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.93% price=78199.9
- Funnel: target 1018 → liquid 218 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +204.94% | $2,555,786.61 |
| CATE/USDT:USDT | +35.41% | $10,831,073.16 |
| JIMOTHY/USDT:USDT | +32.70% | $1,530,424.74 |
| AGI/USDT:USDT | +12.98% | $1,447,792.41 |
| BLESS/USDT:USDT | +11.15% | $9,577,117.43 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DASH/USDT:USDT | below_relative_strength | +5.21% | +4.28% |
| JIMOTHY/USDT:USDT | below_1h_threshold | +4.93% | +4.00% |
| FLOKI/USDT:USDT | below_1h_threshold | +3.76% | +2.83% |
| H/USDT:USDT | below_1h_threshold | +3.66% | +2.73% |
| BLESS/USDT:USDT | below_1h_threshold | +3.63% | +2.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
