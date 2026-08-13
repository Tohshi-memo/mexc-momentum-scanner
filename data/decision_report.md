# Decision Report

- generated_at: 2026-08-13T19:56:45.760646+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11477**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.61% / filled 20/20。**
- 全期間 MARKET基準: n=11477, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.57% | **+1.57%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.61% | **+0.61%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.43% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.37% | **+0.55%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.63% | **+0.33%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.04% | **+0.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$601.25** / 初期 $100.00 (+501.25%)
- 確定: 3981件 (Win 1240 / Loss 1305 / Flat 1436) / skip 4057件
- 成長率目線: 平均log +0.000451 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TUT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.35% 残高後 $601.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.94** / 初期 $100.00 (+49.94%)
- 確定: 1650件 (Win 471 / Loss 397 / Flat 782) / skip 3238件
- 成長率目線: 平均log +0.000245 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0393 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $149.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.97** / 初期 $100.00 (+15.97%)
- 確定: 1468件 (Win 432 / Loss 556 / Flat 480) / pending 2件 / skip 1484件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000055 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $115.97

## 6. Latest Market Context

- 更新: 2026-08-13T19:56:31.028742+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.17% price=63392.2
- Funnel: target 978 → liquid 181 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.7 >= 65=1, 4h RSI 87.1 >= 65=1, 4h RSI 65.8 >= 65=1, 4h RSI 88.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EDEN/USDT:USDT | +25.83% | $4,451,271.53 |
| AKE/USDT:USDT | +23.99% | $39,752,955.33 |
| ACU/USDT:USDT | +11.97% | $9,370,154.35 |
| CATE/USDT:USDT | +11.95% | $1,284,853.44 |
| BLESS/USDT:USDT | +10.78% | $10,068,649.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +4.70% | +4.53% |
| AVAAI/USDT:USDT | below_1h_threshold | +4.36% | +4.19% |
| ACU/USDT:USDT | below_1h_threshold | +3.36% | +3.19% |
| PROM/USDT:USDT | below_1h_threshold | +2.91% | +2.74% |
| BTW/USDT:USDT | below_1h_threshold | +2.79% | +2.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
