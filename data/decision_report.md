# Decision Report

- generated_at: 2026-08-21T18:56:34.592945+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12240**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=12240, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.96% | **+0.81%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_7PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 17/20 | 85.0% | +2.23% | **+1.90%** |
| LIMIT_4PCT_LONG | 16/20 | 80.0% | +2.05% | **+1.64%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +3.17% | **+1.59%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.32% | **+1.39%** |
| LIMIT_9PCT_LONG | 6/20 | 30.0% | +3.70% | **+1.11%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.52** / 初期 $100.00 (+543.52%)
- 確定: 4368件 (Win 1338 / Loss 1435 / Flat 1595) / skip 4433件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $643.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$157.08** / 初期 $100.00 (+57.08%)
- 確定: 1850件 (Win 513 / Loss 440 / Flat 897) / skip 3801件
- 成長率目線: 平均log +0.000244 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0768 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $157.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1896件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000222 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T18:56:20.907105+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.67% price=76862.7
- Funnel: target 1018 → liquid 213 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.0 >= 65=1, 4h RSI 85.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CATE/USDT:USDT | +37.47% | $11,317,336.63 |
| JIMOTHY/USDT:USDT | +28.34% | $1,209,351.70 |
| BICO/USDT:USDT | +10.20% | $3,208,246.03 |
| GPS/USDT:USDT | +9.43% | $3,938,740.61 |
| BEAT/USDT:USDT | +9.16% | $56,941,088.98 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GPS/USDT:USDT | below_1h_threshold | +4.09% | +4.76% |
| ALIGN/USDT:USDT | below_1h_threshold | +2.70% | +3.37% |
| KAITO/USDT:USDT | below_1h_threshold | +2.58% | +3.25% |
| LIT/USDT:USDT | below_1h_threshold | +2.20% | +2.87% |
| RE/USDT:USDT | below_1h_threshold | +2.12% | +2.79% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
