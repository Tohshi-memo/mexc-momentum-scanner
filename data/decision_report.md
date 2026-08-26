# Decision Report

- generated_at: 2026-08-26T05:41:17.762800+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12669**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12669, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.18% | **-2.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 8/20 | 40.0% | +2.20% | **+0.88%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.79% | **+0.35%** |
| LIMIT_6PCT | 8/20 | 40.0% | +0.44% | **+0.18%** |
| LIMIT_9PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.98% | **+2.98%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.69% | **+2.95%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +4.23% | **+2.54%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +3.29% | **+1.81%** |
| LIMIT_BB3S_LONG | 5/13 | 38.5% | +2.52% | **+0.97%** |

## 2. $100 Live Portfolio

- 残高: **$121.16** / 初期 $100.00 (+21.16%)
- 確定トレード: 192件 (TP 73 / SL 114 / EXP 5)
- 最新: CATE/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.16
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$687.36** / 初期 $100.00 (+587.36%)
- 確定: 4585件 (Win 1392 / Loss 1506 / Flat 1687) / skip 4645件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_4PCT_LONG` EXPIRED account +0.00% 残高後 $687.36

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.51** / 初期 $100.00 (+55.51%)
- 確定: 1978件 (Win 536 / Loss 473 / Flat 969) / skip 4102件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0750 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BMT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $155.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.23** / 初期 $100.00 (+15.23%)
- 確定: 1946件 (Win 569 / Loss 742 / Flat 635) / pending 2件 / skip 2191件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000444 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $115.23

## 6. Latest Market Context

- 更新: 2026-08-26T05:41:08.440230+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.30% price=79028.6
- Funnel: target 1023 → liquid 169 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.7 >= 65=1, 4h RSI 87.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BTR/USDT:USDT | +90.53% | $2,461,424.94 |
| PORTAL/USDT:USDT | +44.26% | $1,686,922.96 |
| BMT/USDT:USDT | +38.08% | $11,057,363.86 |
| PONS/USDT:USDT | +28.13% | $1,146,055.94 |
| LONGXIA/USDT:USDT | +23.52% | $1,880,802.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +3.88% | +3.58% |
| BICO/USDT:USDT | below_1h_threshold | +3.52% | +3.22% |
| PONS/USDT:USDT | below_1h_threshold | +2.73% | +2.43% |
| USELESS/USDT:USDT | below_1h_threshold | +2.55% | +2.25% |
| PYTH/USDT:USDT | below_1h_threshold | +1.51% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
