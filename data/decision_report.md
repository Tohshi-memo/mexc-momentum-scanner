# Decision Report

- generated_at: 2026-07-31T19:56:27.819095+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10027**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10027, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/16 | 31.2% | +3.17% | **+0.99%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.92% | **+0.58%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.71% | **+0.54%** |
| LIMIT_1PCT | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.55% | **+2.04%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.29% | **+1.94%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +3.74% | **+1.50%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.52% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$570.30** / 初期 $100.00 (+470.30%)
- 確定: 3581件 (Win 1147 / Loss 1169 / Flat 1265) / skip 3007件
- 成長率目線: 平均log +0.000486 / 幾何平均 +0.049% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BANK/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $570.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1278件 (Win 359 / Loss 297 / Flat 622) / skip 2160件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1142 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MMT/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$112.46** / 初期 $100.00 (+12.46%)
- 確定: 853件 (Win 278 / Loss 336 / Flat 239) / pending 6件 / skip 644件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000367 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $112.46

## 6. Latest Market Context

- 更新: 2026-07-31T19:56:20.582556+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=62982.0
- Funnel: target 921 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +34.15% | $1,105,978.72 |
| GIGGLE/USDT:USDT | +15.42% | $16,210,409.90 |
| KOMA/USDT:USDT | +14.91% | $15,705,598.51 |
| AKE/USDT:USDT | +10.86% | $16,176,796.83 |
| US/USDT:USDT | +10.15% | $1,647,572.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| 1000RATS/USDT:USDT | below_1h_threshold | +4.92% | +5.05% |
| GIGGLE/USDT:USDT | below_1h_threshold | +4.39% | +4.52% |
| US/USDT:USDT | below_1h_threshold | +3.88% | +4.01% |
| KOMA/USDT:USDT | below_1h_threshold | +2.32% | +2.46% |
| GRVT/USDT:USDT | below_1h_threshold | +1.86% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
