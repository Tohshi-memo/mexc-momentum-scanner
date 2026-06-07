# Decision Report

- generated_at: 2026-06-07T05:26:34.429326+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5925**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.94% / filled 20/20。**
- 全期間 MARKET基準: n=5925, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.94%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 20/20 | 100.0% | +1.25% | **+1.25%** |
| MARKET | 20/20 | 100.0% | +0.94% | **+0.94%** |
| ASK | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.77% | **+0.62%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.25% | **+1.30%** |
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +3.38% | **+0.84%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +0.55% | **+0.16%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.71% | **-0.32%** |

## 2. $100 Live Portfolio

- 残高: **$99.99** / 初期 $100.00 (-0.01%)
- 確定トレード: 3件 (TP 1 / SL 2 / EXP 0)
- 最新: LAB/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$137.39** / 初期 $100.00 (+37.39%)
- 確定: 1044件 (Win 251 / Loss 321 / Flat 472) / skip 1442件
- 成長率目線: 平均log +0.000304 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CLO/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $137.39

## 4. Latest Market Context

- 更新: 2026-06-07T05:26:31.218175+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=61842.3
- Funnel: target 771 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +49.41% | $4,091,082.00 |
| LAB/USDT:USDT | +39.52% | $64,354,390.68 |
| BLESS/USDT:USDT | +24.97% | $4,498,126.57 |
| EDEN/USDT:USDT | +18.62% | $1,432,668.06 |
| BIANRENSHENG/USDT:USDT | +16.75% | $1,147,074.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.56% | +3.58% |
| BLESS/USDT:USDT | below_1h_threshold | +3.56% | +3.58% |
| CLO/USDT:USDT | below_1h_threshold | +3.50% | +3.52% |
| ZEC/USDT:USDT | below_1h_threshold | +3.07% | +3.09% |
| ASTER/USDT:USDT | below_1h_threshold | +2.61% | +2.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
