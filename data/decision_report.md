# Decision Report

- generated_at: 2026-09-25T10:46:28.125436+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15520**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15520, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +3.53% | **+1.59%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.93% | **+1.54%** |
| LIMIT_3PCT | 14/20 | 70.0% | +2.01% | **+1.40%** |
| LIMIT_6PCT | 5/20 | 25.0% | +5.55% | **+1.39%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.09% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.41% | **+1.45%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +0.92% | **+0.64%** |
| LIMIT_BB3S_LONG | 8/8 | 100.0% | +0.56% | **+0.56%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.01% | **+0.46%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +0.30% | **+0.27%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,206.94** / 初期 $100.00 (+1106.94%)
- 確定: 5901件 (Win 1740 / Loss 1890 / Flat 2271) / skip 6180件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.76% 残高後 $1,206.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$256.32** / 初期 $100.00 (+156.32%)
- 確定: 3453件 (Win 952 / Loss 793 / Flat 1708) / skip 5478件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0567 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_5PCT` TP_HIT account +0.69% 残高後 $256.32

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 0件 / skip 3821件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000200 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T10:46:14.954189+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.24% price=84728.4
- Funnel: target 1069 → liquid 176 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARK/USDT:USDT | +28.23% | $1,422,697.71 |
| PHA/USDT:USDT | +23.93% | $2,210,672.50 |
| QNT/USDT:USDT | +20.52% | $14,914,231.11 |
| GRASS/USDT:USDT | +16.18% | $1,135,034.58 |
| SYN/USDT:USDT | +14.45% | $3,599,480.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_relative_strength | +5.14% | +4.90% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +3.76% | +3.53% |
| PHA/USDT:USDT | below_1h_threshold | +3.11% | +2.87% |
| QNT/USDT:USDT | below_1h_threshold | +3.10% | +2.87% |
| ZRO/USDT:USDT | below_1h_threshold | +2.74% | +2.50% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
