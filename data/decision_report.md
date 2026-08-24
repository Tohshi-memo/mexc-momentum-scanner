# Decision Report

- generated_at: 2026-08-24T03:26:27.008798+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12488**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.08% / filled 20/20。**
- 全期間 MARKET基準: n=12488, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.08% | **+2.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.08% | **+2.08%** |
| LIMIT_ATR | 13/20 | 65.0% | +3.16% | **+2.05%** |
| LIMIT_1PCT | 17/20 | 85.0% | +2.30% | **+1.95%** |
| LIMIT_BB3S | 5/17 | 29.4% | +2.64% | **+0.78%** |
| LIMIT_2PCT | 12/20 | 60.0% | +0.77% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 16/20 | 80.0% | +0.91% | **+0.73%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +1.10% | **+0.66%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |
| LIMIT_6PCT_LONG | 14/20 | 70.0% | +0.68% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$121.29** / 初期 $100.00 (+21.29%)
- 確定トレード: 191件 (TP 73 / SL 113 / EXP 5)
- 最新: ON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.29
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$703.82** / 初期 $100.00 (+603.82%)
- 確定: 4509件 (Win 1375 / Loss 1477 / Flat 1657) / skip 4540件
- 成長率目線: 平均log +0.000433 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $703.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.71** / 初期 $100.00 (+56.71%)
- 確定: 1964件 (Win 536 / Loss 470 / Flat 958) / skip 3935件
- 成長率目線: 平均log +0.000229 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0145 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LIT/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $156.71

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.54** / 初期 $100.00 (+16.54%)
- 確定: 1874件 (Win 551 / Loss 709 / Flat 614) / pending 4件 / skip 2081件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000232 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: LIT/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.17% 残高後 $116.54

## 6. Latest Market Context

- 更新: 2026-08-24T03:26:17.400695+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.31% price=77221.2
- Funnel: target 1018 → liquid 177 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1, 4h RSI 76.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CASHCAT/USDT:USDT | +22.07% | $1,085,182.11 |
| BASECAT/USDT:USDT | +14.76% | $2,968,275.46 |
| TUT/USDT:USDT | +13.21% | $51,553,867.26 |
| LIT/USDT:USDT | +11.02% | $13,851,050.86 |
| GRASS/USDT:USDT | +8.60% | $3,226,416.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GRASS/USDT:USDT | below_1h_threshold | +3.15% | +3.45% |
| UP/USDT:USDT | below_1h_threshold | +2.45% | +2.76% |
| ACE/USDT:USDT | below_1h_threshold | +2.16% | +2.47% |
| FF/USDT:USDT | below_1h_threshold | +2.00% | +2.31% |
| CYS/USDT:USDT | below_1h_threshold | +1.11% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
