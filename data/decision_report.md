# Decision Report

- generated_at: 2026-09-01T10:41:26.073824+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13243**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.39% / filled 20/20。**
- 全期間 MARKET基準: n=13243, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.39% | **+0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.94% | **+0.66%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_BB3S | 4/15 | 26.7% | +2.22% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.34% | **+0.87%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +1.73% | **+0.69%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.60% | **+0.45%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.42% | **+0.43%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.22% | **+0.18%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 196件 (TP 73 / SL 118 / EXP 5)
- 最新: BTR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$797.75** / 初期 $100.00 (+697.75%)
- 確定: 4879件 (Win 1486 / Loss 1609 / Flat 1784) / skip 4925件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $797.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$172.86** / 初期 $100.00 (+72.86%)
- 確定: 2222件 (Win 618 / Loss 539 / Flat 1065) / skip 4432件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0240 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $172.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.28** / 初期 $100.00 (+15.28%)
- 確定: 2087件 (Win 610 / Loss 815 / Flat 662) / pending 0件 / skip 2627件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000327 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.28

## 6. Latest Market Context

- 更新: 2026-09-01T10:41:16.338465+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.31% price=78115.5
- Funnel: target 1034 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +31.24% | $24,094,585.58 |
| ARB/USDT:USDT | +27.96% | $80,625,770.41 |
| ONG/USDT:USDT | +16.86% | $4,499,266.01 |
| CRV/USDT:USDT | +14.49% | $6,619,482.44 |
| OP/USDT:USDT | +13.98% | $8,568,421.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TUT/USDT:USDT | below_1h_threshold | +4.55% | +4.24% |
| ENA/USDT:USDT | below_1h_threshold | +4.00% | +3.69% |
| ONG/USDT:USDT | below_1h_threshold | +3.34% | +3.03% |
| OP/USDT:USDT | below_1h_threshold | +3.32% | +3.01% |
| HEMI/USDT:USDT | below_1h_threshold | +3.30% | +2.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
