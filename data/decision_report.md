# Decision Report

- generated_at: 2026-05-12T16:38:19.870846+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4144**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.76% / filled 20/20。**
- 全期間 MARKET基準: n=4144, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=+0.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.03% | **+1.03%** |
| MARKET | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.30% | **+0.27%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.60% | **+1.36%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.06% | **+0.74%** |
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.56% | **+0.39%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.65** / 初期 $100.00 (+19.65%)
- 確定: 280件 (Win 80 / Loss 96 / Flat 104) / skip 425件
- 成長率目線: 平均log +0.000641 / 幾何平均 +0.064% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VIC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $119.65

## 4. Latest Market Context

- 更新: 2026-05-12T16:38:16.667812+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80274.9
- Funnel: target 763 → liquid 197 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.8 >= 65=1, 4h RSI 75.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VIC/USDT:USDT | +18.39% | $2,373,667.14 |
| UP/USDT:USDT | +8.23% | $1,736,533.47 |
| COAI/USDT:USDT | +4.95% | $1,040,776.29 |
| XNY/USDT:USDT | +3.92% | $1,329,358.92 |
| SAGA/USDT:USDT | +3.45% | $38,273,626.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COAI/USDT:USDT | below_1h_threshold | +4.81% | +4.85% |
| XNY/USDT:USDT | below_1h_threshold | +3.92% | +3.96% |
| SAGA/USDT:USDT | below_1h_threshold | +3.53% | +3.57% |
| IRYS/USDT:USDT | below_1h_threshold | +3.38% | +3.41% |
| GUA/USDT:USDT | below_1h_threshold | +3.33% | +3.37% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
