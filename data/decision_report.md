# Decision Report

- generated_at: 2026-08-18T14:36:34.488797+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11909**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.33% / filled 20/20。**
- 全期間 MARKET基準: n=11909, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+1.33%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.33% | **+1.33%** |
| LIMIT_BB3S | 3/17 | 17.6% | +3.77% | **+0.67%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_4PCT | 11/20 | 55.0% | +1.10% | **+0.60%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.54% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +6.27% | **+1.25%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +3.00% | **+1.20%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.63% | **+1.06%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.12% | **+0.50%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.58% | **+0.43%** |

## 2. $100 Live Portfolio

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定トレード: 187件 (TP 72 / SL 110 / EXP 5)
- 最新: HEMI/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.41
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$615.65** / 初期 $100.00 (+515.65%)
- 確定: 4209件 (Win 1295 / Loss 1374 / Flat 1540) / skip 4261件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 1000RATS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $615.65

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.25** / 初期 $100.00 (+55.25%)
- 確定: 1820件 (Win 502 / Loss 427 / Flat 891) / skip 3500件
- 成長率目線: 平均log +0.000242 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0067 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ACE/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $155.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.43** / 初期 $100.00 (+18.43%)
- 確定: 1717件 (Win 513 / Loss 653 / Flat 551) / pending 6件 / skip 1662件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000213 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $118.43

## 6. Latest Market Context

- 更新: 2026-08-18T14:36:27.544095+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.95% price=64796.6
- Funnel: target 993 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +31.49% | $40,153,620.36 |
| 1000RATS/USDT:USDT | +29.18% | $2,761,425.48 |
| CLO/USDT:USDT | +26.40% | $1,041,982.27 |
| PRL/USDT:USDT | +20.79% | $3,983,588.11 |
| SOXS/USDT:USDT | +18.33% | $14,454,646.86 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ACE/USDT:USDT | below_1h_threshold | +4.14% | +3.19% |
| SOXS/USDT:USDT | below_1h_threshold | +2.55% | +1.60% |
| ORDI/USDT:USDT | below_1h_threshold | +2.52% | +1.57% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +1.93% | +0.99% |
| BMT/USDT:USDT | below_1h_threshold | +1.85% | +0.91% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
