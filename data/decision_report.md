# Decision Report

- generated_at: 2026-08-25T22:56:19.965694+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12639**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12639, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.22% | **-0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +1.93% | **+0.77%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.57% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.68% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.79% | **+2.09%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.52% | **+2.02%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +3.03% | **+1.51%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.56% | **+1.48%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.80% | **+1.35%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$687.36** / 初期 $100.00 (+587.36%)
- 確定: 4584件 (Win 1392 / Loss 1506 / Flat 1686) / skip 4616件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BMT/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $687.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1978件 (Win 536 / Loss 473 / Flat 969) / skip 4072件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0386 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$113.86** / 初期 $100.00 (+13.86%)
- 確定: 1934件 (Win 564 / Loss 740 / Flat 630) / pending 0件 / skip 2176件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.17% 残高後 $113.86

## 6. Latest Market Context

- 更新: 2026-08-25T22:56:09.952851+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=78831.7
- Funnel: target 1023 → liquid 183 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LONGXIA/USDT:USDT | +50.31% | $1,156,213.86 |
| BMT/USDT:USDT | +46.74% | $6,605,214.31 |
| STAR/USDT:USDT | +8.11% | $1,034,497.72 |
| AGI/USDT:USDT | +7.89% | $1,992,099.66 |
| PROM/USDT:USDT | +3.92% | $12,839,113.20 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BMT/USDT:USDT | below_1h_threshold | +4.09% | +3.71% |
| TAC/USDT:USDT | below_1h_threshold | +3.32% | +2.94% |
| STAR/USDT:USDT | below_1h_threshold | +2.46% | +2.09% |
| CHIP/USDT:USDT | below_1h_threshold | +1.87% | +1.50% |
| USELESS/USDT:USDT | below_1h_threshold | +1.82% | +1.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
