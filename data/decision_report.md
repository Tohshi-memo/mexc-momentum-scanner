# Decision Report

- generated_at: 2026-07-25T23:56:22.945924+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9547**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.38% / filled 20/20。**
- 全期間 MARKET基準: n=9547, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.38%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.38% | **+0.38%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.01% | **+0.35%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.27% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.40% | **+1.33%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.35% | **+1.08%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.32% | **+0.66%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$456.53** / 初期 $100.00 (+356.53%)
- 確定: 3375件 (Win 1072 / Loss 1095 / Flat 1208) / skip 2733件
- 成長率目線: 平均log +0.000450 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EUL/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $456.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.69** / 初期 $100.00 (+37.69%)
- 確定: 1200件 (Win 332 / Loss 265 / Flat 603) / skip 1758件
- 成長率目線: 平均log +0.000267 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1061 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $137.69

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.07** / 初期 $100.00 (+8.07%)
- 確定: 591件 (Win 200 / Loss 228 / Flat 163) / pending 3件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000470 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EUL/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $108.07

## 6. Latest Market Context

- 更新: 2026-07-25T23:56:15.262015+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=64332.0
- Funnel: target 898 → liquid 118 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.1 >= 65=1, 4h RSI 79.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +33.33% | $20,763,230.32 |
| ESPORTS/USDT:USDT | +27.46% | $26,968,726.49 |
| ALLO/USDT:USDT | +15.02% | $18,332,210.79 |
| BANK/USDT:USDT | +14.50% | $88,487,452.80 |
| VELVET/USDT:USDT | +9.01% | $8,183,757.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_1h_threshold | +2.65% | +2.72% |
| LAB/USDT:USDT | below_1h_threshold | +2.62% | +2.69% |
| EVAA/USDT:USDT | below_1h_threshold | +1.76% | +1.83% |
| GRAM/USDT:USDT | below_1h_threshold | +1.01% | +1.08% |
| SHIB/USDT:USDT | below_1h_threshold | +0.85% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
