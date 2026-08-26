# Decision Report

- generated_at: 2026-08-26T13:20:58.143955+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12706**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.64% / filled 20/20。**
- 全期間 MARKET基準: n=12706, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.64%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.64% | **+1.64%** |
| LIMIT_1PCT | 19/20 | 95.0% | +1.52% | **+1.45%** |
| LIMIT_BB3S | 9/17 | 52.9% | +2.42% | **+1.28%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.42% | **+1.07%** |
| LIMIT_ATR | 15/20 | 75.0% | +1.23% | **+0.92%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +0.66% | **+0.36%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.41% | **+0.31%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.34% | **+0.26%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.10% | **+0.16%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.40% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$693.49** / 初期 $100.00 (+593.49%)
- 確定: 4605件 (Win 1400 / Loss 1515 / Flat 1690) / skip 4662件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $693.49

## 4. Robust Adaptive DryRun ($100)

- 残高: **$156.51** / 初期 $100.00 (+56.51%)
- 確定: 2001件 (Win 544 / Loss 483 / Flat 974) / skip 4116件
- 成長率目線: 平均log +0.000224 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0688 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $156.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.20** / 初期 $100.00 (+16.20%)
- 確定: 1978件 (Win 580 / Loss 755 / Flat 643) / pending 2件 / skip 2195件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000320 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BICO/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.20

## 6. Latest Market Context

- 更新: 2026-08-26T12:51:07.730712+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=78337.4
- Funnel: target 1023 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +261.27% | $18,596,670.06 |
| BMT/USDT:USDT | +48.17% | $16,084,806.79 |
| TAC/USDT:USDT | +44.57% | $7,917,510.14 |
| LONGXIA/USDT:USDT | +32.49% | $1,997,404.48 |
| BICO/USDT:USDT | +18.94% | $3,823,676.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LONGXIA/USDT:USDT | below_1h_threshold | +3.03% | +3.16% |
| CYS/USDT:USDT | below_1h_threshold | +2.99% | +3.12% |
| WIF/USDT:USDT | below_1h_threshold | +1.59% | +1.73% |
| SPX/USDT:USDT | below_1h_threshold | +1.59% | +1.73% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.27% | +1.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
