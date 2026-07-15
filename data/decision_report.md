# Decision Report

- generated_at: 2026-07-15T21:06:21.373549+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8765**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.23% / filled 20/20。**
- 全期間 MARKET基準: n=8765, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.23% | **+2.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.23% | **+2.23%** |
| LIMIT_1PCT | 18/20 | 90.0% | +2.15% | **+1.93%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.25% | **+1.69%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.69% | **+1.10%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.74% | **+0.96%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +0.14% | **+0.14%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.56% | **-0.31%** |

## 2. $100 Live Portfolio

- 残高: **$103.22** / 初期 $100.00 (+3.22%)
- 確定トレード: 99件 (TP 34 / SL 63 / EXP 2)
- 最新: LAB/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.89** / 初期 $100.00 (+242.89%)
- 確定: 2884件 (Win 903 / Loss 938 / Flat 1043) / skip 2442件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ROAM/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $342.89

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.40** / 初期 $100.00 (+5.40%)
- 確定: 729件 (Win 167 / Loss 168 / Flat 394) / skip 1447件
- 成長率目線: 平均log +0.000072 / 幾何平均 +0.007% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0942 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ONDO/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $105.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.49** / 初期 $100.00 (-1.51%)
- 確定: 64件 (Win 19 / Loss 41 / Flat 4) / pending 0件 / skip 175件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000239 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XEC/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.09% 残高後 $98.49

## 6. Latest Market Context

- 更新: 2026-07-15T21:06:13.495267+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64920.8
- Funnel: target 871 → liquid 168 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.5 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ROAM/USDT:USDT | +93.28% | $3,496,594.91 |
| SKL/USDT:USDT | +13.76% | $1,639,728.97 |
| CAP/USDT:USDT | +12.97% | $1,329,133.93 |
| HOME/USDT:USDT | +10.01% | $1,048,854.11 |
| SNXX/USDT:USDT | +9.37% | $1,324,975.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DEXE/USDT:USDT | below_1h_threshold | +3.42% | +3.45% |
| LDO/USDT:USDT | below_1h_threshold | +0.77% | +0.80% |
| EIGEN/USDT:USDT | below_1h_threshold | +0.53% | +0.56% |
| ETHFI/USDT:USDT | below_1h_threshold | +0.48% | +0.50% |
| SEI/USDT:USDT | below_1h_threshold | +0.45% | +0.48% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
