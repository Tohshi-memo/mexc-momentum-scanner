# Decision Report

- generated_at: 2026-06-05T17:03:13.454038+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5731**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.60% / filled 20/20。**
- 全期間 MARKET基準: n=5731, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +3.13% | **+3.13%** |
| MARKET | 20/20 | 100.0% | +2.60% | **+2.60%** |
| LIMIT_1PCT | 19/20 | 95.0% | +2.59% | **+2.46%** |
| LIMIT_2PCT | 16/20 | 80.0% | +2.76% | **+2.21%** |
| LIMIT_ATR | 12/20 | 60.0% | +1.84% | **+1.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_8PCT_LONG | 11/20 | 55.0% | +2.18% | **+1.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +0.57% | **+0.32%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +0.09% | **+0.06%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | -0.06% | **-0.05%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1011件 (Win 239 / Loss 313 / Flat 459) / skip 1281件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HOME/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-05T17:03:10.996513+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=61193.9
- Funnel: target 773 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EPIC/USDT:USDT | +15.01% | $2,771,495.93 |
| ZEC/USDT:USDT | +11.17% | $1,146,478,810.10 |
| HOME/USDT:USDT | +8.17% | $8,104,770.02 |
| ENA/USDT:USDT | +6.24% | $47,854,293.28 |
| GUA/USDT:USDT | +6.09% | $1,801,973.67 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +3.66% | +3.93% |
| GUA/USDT:USDT | below_1h_threshold | +1.83% | +2.10% |
| EPIC/USDT:USDT | below_1h_threshold | +1.13% | +1.41% |
| ZEC/USDT:USDT | below_1h_threshold | +1.13% | +1.40% |
| LDO/USDT:USDT | below_1h_threshold | +0.80% | +1.07% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
