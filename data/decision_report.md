# Decision Report

- generated_at: 2026-08-26T11:41:17.765509+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12700**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.44% / filled 20/20。**
- 全期間 MARKET基準: n=12700, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 17/20 | 85.0% | +1.39% | **+1.18%** |
| LIMIT_BB3S | 7/18 | 38.9% | +2.54% | **+0.99%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.44% | **+0.44%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.37% | **+0.35%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.08% | **+1.03%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.45% | **+1.02%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.80% | **+0.64%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +0.92% | **+0.37%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.52% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$704.00** / 初期 $100.00 (+604.00%)
- 確定: 4600件 (Win 1400 / Loss 1512 / Flat 1688) / skip 4661件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BMT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $704.00

## 4. Robust Adaptive DryRun ($100)

- 残高: **$158.72** / 初期 $100.00 (+58.72%)
- 確定: 1995件 (Win 544 / Loss 479 / Flat 972) / skip 4116件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1467 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $158.72

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.02** / 初期 $100.00 (+17.02%)
- 確定: 1972件 (Win 580 / Loss 751 / Flat 641) / pending 6件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000409 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.02

## 6. Latest Market Context

- 更新: 2026-08-26T11:41:08.299618+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.42% price=78355.4
- Funnel: target 1023 → liquid 169 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +247.64% | $16,581,739.21 |
| BMT/USDT:USDT | +52.38% | $15,495,410.42 |
| TAC/USDT:USDT | +51.75% | $7,305,096.59 |
| LONGXIA/USDT:USDT | +28.32% | $1,987,758.69 |
| PONS/USDT:USDT | +22.06% | $1,145,632.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTR/USDT:USDT | below_1h_threshold | +3.57% | +3.99% |
| LONGXIA/USDT:USDT | below_1h_threshold | +2.13% | +2.55% |
| STX/USDT:USDT | below_1h_threshold | +1.27% | +1.69% |
| LIGHT/USDT:USDT | below_1h_threshold | +0.75% | +1.17% |
| SKYAI/USDT:USDT | below_1h_threshold | +0.50% | +0.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
