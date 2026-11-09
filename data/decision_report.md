# Decision Report

- generated_at: 2026-11-09T11:46:33.202671+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18520**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.22% / filled 20/20。**
- 全期間 MARKET基準: n=18520, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.22%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.22% | **+0.22%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +4.20% | **+1.47%** |
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.24% | **+0.93%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 18/20 | 90.0% | +2.48% | **+2.24%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +2.69% | **+2.15%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.30% | **+1.49%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +1.53% | **+1.38%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.07% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定トレード: 266件 (TP 97 / SL 161 / EXP 8)
- 最新: AKE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.37
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,626.14** / 初期 $100.00 (+1526.14%)
- 確定: 7163件 (Win 2057 / Loss 2285 / Flat 2821) / skip 7918件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RITUAL/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,626.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4757件 (Win 1277 / Loss 1047 / Flat 2433) / skip 7174件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0602 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6682件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000251 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-09T11:46:19.750789+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.54% price=74527.9
- Funnel: target 1090 → liquid 141 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1, 4h RSI 81.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ON/USDT:USDT | +42.40% | $1,748,527.29 |
| RITUAL/USDT:USDT | +30.65% | $1,625,862.43 |
| PIEVERSE/USDT:USDT | +17.56% | $1,585,311.78 |
| IDOL/USDT:USDT | +11.78% | $2,887,238.34 |
| ANSEM/USDT:USDT | +8.58% | $1,147,393.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_relative_strength | +5.28% | +4.74% |
| AKE/USDT:USDT | below_1h_threshold | +3.27% | +2.73% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.56% | +2.02% |
| ON/USDT:USDT | below_1h_threshold | +2.39% | +1.85% |
| STRK/USDT:USDT | below_1h_threshold | +1.75% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
