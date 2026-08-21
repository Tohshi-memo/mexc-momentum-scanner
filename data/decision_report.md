# Decision Report

- generated_at: 2026-08-21T19:41:30.039214+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12245**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.78% / filled 20/20。**
- 全期間 MARKET基準: n=12245, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.78%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.78% | **+0.78%** |
| LIMIT_BB3S | 5/16 | 31.2% | +2.48% | **+0.77%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.49%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.53% | **+0.42%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +3.14% | **+3.14%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.51% | **+1.14%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.78% | **+0.89%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.98% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$643.52** / 初期 $100.00 (+543.52%)
- 確定: 4371件 (Win 1338 / Loss 1435 / Flat 1598) / skip 4435件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $643.52

## 4. Robust Adaptive DryRun ($100)

- 残高: **$155.98** / 初期 $100.00 (+55.98%)
- 確定: 1855件 (Win 513 / Loss 442 / Flat 900) / skip 3801件
- 成長率目線: 平均log +0.000240 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0509 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $155.98

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.90** / 初期 $100.00 (+16.90%)
- 確定: 1824件 (Win 540 / Loss 693 / Flat 591) / pending 0件 / skip 1899件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000202 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: UNITREE/USDT:USDT `MARKET_LONG` EXPIRED account -0.09% 残高後 $116.90

## 6. Latest Market Context

- 更新: 2026-08-21T19:41:17.339039+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77087.0
- Funnel: target 1018 → liquid 217 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.3 >= 65=1, 4h RSI 87.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +155.67% | $1,587,869.87 |
| CATE/USDT:USDT | +40.76% | $11,097,943.15 |
| JIMOTHY/USDT:USDT | +25.69% | $1,363,012.61 |
| COTI/USDT:USDT | +11.25% | $1,500,729.18 |
| LIT/USDT:USDT | +10.60% | $11,730,016.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CATE/USDT:USDT | below_1h_threshold | +4.61% | +4.64% |
| LIT/USDT:USDT | below_1h_threshold | +2.23% | +2.26% |
| BTW/USDT:USDT | below_1h_threshold | +1.49% | +1.52% |
| ACE/USDT:USDT | below_1h_threshold | +1.47% | +1.50% |
| VELVET/USDT:USDT | below_1h_threshold | +1.18% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
