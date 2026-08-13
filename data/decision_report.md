# Decision Report

- generated_at: 2026-08-13T14:41:55.911074+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11448**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11448, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +1.62% | **+1.38%** |
| LIMIT_BB3S | 5/13 | 38.5% | +2.79% | **+1.07%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.03% | **+0.98%** |
| LIMIT_ATR | 16/20 | 80.0% | +1.20% | **+0.96%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.86% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.96% | **+0.88%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.97% | **+0.44%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +2.45% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$613.05** / 初期 $100.00 (+513.05%)
- 確定: 3966件 (Win 1238 / Loss 1297 / Flat 1431) / skip 4043件
- 成長率目線: 平均log +0.000457 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $613.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$150.66** / 初期 $100.00 (+50.66%)
- 確定: 1636件 (Win 467 / Loss 390 / Flat 779) / skip 3223件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1175 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $150.66

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.19** / 初期 $100.00 (+16.19%)
- 確定: 1453件 (Win 427 / Loss 547 / Flat 479) / pending 5件 / skip 1467件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000230 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.19

## 6. Latest Market Context

- 更新: 2026-08-13T14:41:43.104545+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=63919.2
- Funnel: target 978 → liquid 178 → pre 50 → checked 50 → surge 7 → strict 0
- Surge前reject: below_1h_threshold=42, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.9 >= 65=1, 4h RSI 79.6 >= 65=1, 4h RSI 84.0 >= 65=1, 4h RSI 83.1 >= 65=1, 4h RSI 73.6 >= 65=1, 4h RSI 71.4 >= 65=1, 4h RSI 77.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +50.35% | $23,517,662.44 |
| ACU/USDT:USDT | +30.78% | $7,683,135.97 |
| COTI/USDT:USDT | +25.15% | $11,658,341.13 |
| AVNT/USDT:USDT | +23.43% | $2,104,868.38 |
| BTW/USDT:USDT | +21.08% | $24,516,464.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_relative_strength | +5.10% | +4.75% |
| SMCISTOCK/USDT:USDT | below_1h_threshold | +4.69% | +4.35% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +4.58% | +4.23% |
| AVNT/USDT:USDT | below_1h_threshold | +4.44% | +4.09% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +4.21% | +3.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
