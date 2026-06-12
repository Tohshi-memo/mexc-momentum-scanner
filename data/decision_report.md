# Decision Report

- generated_at: 2026-06-12T10:21:03.099629+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6499**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.11% / filled 20/20。**
- 全期間 MARKET基準: n=6499, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=+1.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.11% | **+1.11%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.01% | **+0.91%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.02% | **+0.76%** |
| LIMIT_BB3S | 5/19 | 26.3% | +2.48% | **+0.65%** |
| LIMIT_ATR | 11/20 | 55.0% | +0.97% | **+0.53%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +2.22% | **+0.44%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.30% | **+0.17%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +0.19% | **+0.09%** |
| ASK_LONG | 20/20 | 100.0% | +0.09% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$95.17** / 初期 $100.00 (-4.83%)
- 確定トレード: 17件 (TP 2 / SL 14 / EXP 1)
- 最新: ZBT/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.17
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$166.39** / 初期 $100.00 (+66.39%)
- 確定: 1373件 (Win 375 / Loss 442 / Flat 556) / skip 1687件
- 成長率目線: 平均log +0.000371 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NAORIS/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $166.39

## 4. Latest Market Context

- 更新: 2026-06-12T10:21:00.099545+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=63711.3
- Funnel: target 769 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +96.01% | $151,998,942.19 |
| ESPORTS/USDT:USDT | +78.40% | $42,773,574.80 |
| XPL/USDT:USDT | +38.84% | $11,114,243.67 |
| NAORIS/USDT:USDT | +37.19% | $4,262,992.75 |
| AIN/USDT:USDT | +32.74% | $1,073,974.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COAI/USDT:USDT | below_1h_threshold | +5.00% | +5.02% |
| AIN/USDT:USDT | below_1h_threshold | +2.10% | +2.12% |
| OP/USDT:USDT | below_1h_threshold | +1.52% | +1.55% |
| XMR/USDT:USDT | below_1h_threshold | +1.41% | +1.44% |
| LAB/USDT:USDT | below_1h_threshold | +0.67% | +0.70% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
