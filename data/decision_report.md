# Decision Report

- generated_at: 2026-08-13T15:36:32.337924+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11455**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11455, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.93% | **-1.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 18/20 | 90.0% | +0.38% | **+0.34%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_2PCT | 19/20 | 95.0% | +0.09% | **+0.09%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +4.57% | **+1.60%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.28% | **+1.48%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| MARKET_LONG | 20/20 | 100.0% | +0.93% | **+0.93%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$613.01** / 初期 $100.00 (+513.01%)
- 確定: 3973件 (Win 1239 / Loss 1299 / Flat 1435) / skip 4043件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AVAAI/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $613.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$151.94** / 初期 $100.00 (+51.94%)
- 確定: 1643件 (Win 470 / Loss 392 / Flat 781) / skip 3223件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0862 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AVAAI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $151.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.00** / 初期 $100.00 (+17.00%)
- 確定: 1458件 (Win 430 / Loss 548 / Flat 480) / pending 5件 / skip 1467件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000240 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AVAAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.00

## 6. Latest Market Context

- 更新: 2026-08-13T15:36:22.445443+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=63657.3
- Funnel: target 978 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +54.17% | $26,065,681.36 |
| AVAAI/USDT:USDT | +34.90% | $1,924,488.92 |
| ACU/USDT:USDT | +29.67% | $8,100,491.78 |
| COTI/USDT:USDT | +28.52% | $11,891,374.18 |
| AVNT/USDT:USDT | +24.21% | $2,987,128.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SMCISTOCK/USDT:USDT | below_1h_threshold | +4.78% | +5.06% |
| BR/USDT:USDT | below_1h_threshold | +4.48% | +4.76% |
| MUU/USDT:USDT | below_1h_threshold | +3.30% | +3.58% |
| AKE/USDT:USDT | below_1h_threshold | +3.28% | +3.56% |
| CIENSTOCK/USDT:USDT | below_1h_threshold | +3.17% | +3.45% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
