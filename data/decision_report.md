# Decision Report

- generated_at: 2026-05-07T14:22:38.181584+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3640**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3640, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-1.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.27% | **-1.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_5PCT | 12/20 | 60.0% | +1.48% | **+0.89%** |
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +5.24% | **+2.88%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +4.96% | **+2.73%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +6.05% | **+2.72%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +4.12% | **+2.68%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +6.70% | **+2.35%** |

## 2. $100 Live Portfolio

- 残高: **$100.83** / 初期 $100.00 (+0.83%)
- 確定トレード: 20件 (TP 6 / SL 12 / EXP 2)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.83
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$112.33** / 初期 $100.00 (+12.33%)
- 確定: 134件 (Win 44 / Loss 48 / Flat 42) / skip 67件
- 成長率目線: 平均log +0.000867 / 幾何平均 +0.087% per trade / maxDD +2.62%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SATO/USDT:USDT `LIMIT_6PCT_LONG` EXPIRED account +0.00% 残高後 $112.33

## 4. Latest Market Context

- 更新: 2026-05-07T14:22:34.395449+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=80428.2
- Funnel: target 771 → liquid 185 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.4 >= 65=1, 4h RSI 92.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SATO/USDT:USDT | +108.27% | $3,435,326.42 |
| B3/USDT:USDT | +92.42% | $10,875,907.78 |
| PENGUIN/USDT:USDT | +84.35% | $4,161,924.48 |
| NIL/USDT:USDT | +49.66% | $4,244,295.77 |
| DOGS/USDT:USDT | +47.62% | $17,465,540.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MUSTOCK/USDT:USDT | below_1h_threshold | +3.40% | +3.44% |
| SIREN/USDT:USDT | below_1h_threshold | +2.34% | +2.38% |
| NVIDIA/USDT:USDT | below_1h_threshold | +2.28% | +2.32% |
| JTO/USDT:USDT | below_1h_threshold | +2.22% | +2.26% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +2.06% | +2.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
