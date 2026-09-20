# Decision Report

- generated_at: 2026-09-20T00:51:24.118799+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15116**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.36% / filled 20/20。**
- 全期間 MARKET基準: n=15116, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.36%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.36% | **+1.36%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.79% | **+0.71%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.29% | **+0.23%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.26% | **+0.18%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | -0.89% | **-0.09%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,210.23** / 初期 $100.00 (+1110.23%)
- 確定: 5645件 (Win 1694 / Loss 1829 / Flat 2122) / skip 6032件
- 成長率目線: 平均log +0.000442 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CELR/USDT:USDT `LIMIT_5PCT` TP_HIT account +1.00% 残高後 $1,210.23

## 4. Robust Adaptive DryRun ($100)

- 残高: **$246.61** / 初期 $100.00 (+146.61%)
- 確定: 3229件 (Win 896 / Loss 762 / Flat 1571) / skip 5298件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0644 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CELR/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $246.61

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.58** / 初期 $100.00 (+21.58%)
- 確定: 2977件 (Win 880 / Loss 1178 / Flat 919) / pending 1件 / skip 3610件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000198 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CNPY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.58

## 6. Latest Market Context

- 更新: 2026-09-20T00:51:10.857851+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=81252.1
- Funnel: target 1050 → liquid 142 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CELR/USDT:USDT | +72.53% | $1,615,029.14 |
| OFC/USDT:USDT | +51.23% | $1,886,635.69 |
| ONE/USDT:USDT | +26.69% | $47,506,356.77 |
| EVAA/USDT:USDT | +13.88% | $1,382,438.96 |
| BANK/USDT:USDT | +13.06% | $2,697,794.51 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVAX/USDT:USDT | below_1h_threshold | +3.95% | +3.91% |
| INJ/USDT:USDT | below_1h_threshold | +3.61% | +3.57% |
| ZIL/USDT:USDT | below_1h_threshold | +3.59% | +3.55% |
| ALGO/USDT:USDT | below_1h_threshold | +2.99% | +2.95% |
| G/USDT:USDT | below_1h_threshold | +2.95% | +2.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
